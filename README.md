# SyndProxy validated proxy pool

## Current pool

- Alive now: 663
- Gold now: 424
- HTTP: 123 alive / 76 gold
- HTTPS: 180 alive / 25 gold
- SOCKS4: 173 alive / 157 gold
- SOCKS5: 187 alive / 166 gold

## Historical pool

- Discovered: 190445
- Ever alive: 40494
- Ever gold: 1310

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
