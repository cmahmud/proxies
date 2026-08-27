# SyndProxy validated proxy pool

## Current pool

- Alive now: 623
- Gold now: 393
- HTTP: 99 alive / 58 gold
- HTTPS: 159 alive / 14 gold
- SOCKS4: 173 alive / 157 gold
- SOCKS5: 192 alive / 164 gold

## Historical pool

- Discovered: 190445
- Ever alive: 41091
- Ever gold: 1317

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
