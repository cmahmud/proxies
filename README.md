# SyndProxy validated proxy pool

## Current pool

- Alive now: 519
- Gold now: 402
- HTTP: 102 alive / 60 gold
- HTTPS: 60 alive / 17 gold
- SOCKS4: 174 alive / 161 gold
- SOCKS5: 183 alive / 164 gold

## Historical pool

- Discovered: 185576
- Ever alive: 39048
- Ever gold: 1296

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
