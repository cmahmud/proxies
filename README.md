# SyndProxy validated proxy pool

## Current pool

- Alive now: 634
- Gold now: 384
- HTTP: 128 alive / 71 gold
- HTTPS: 175 alive / 17 gold
- SOCKS4: 157 alive / 146 gold
- SOCKS5: 174 alive / 150 gold

## Historical pool

- Discovered: 190445
- Ever alive: 39883
- Ever gold: 1304

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
