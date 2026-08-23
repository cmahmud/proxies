# SyndProxy validated proxy pool

## Current pool

- Alive now: 481
- Gold now: 384
- HTTP: 87 alive / 56 gold
- HTTPS: 55 alive / 13 gold
- SOCKS4: 163 alive / 155 gold
- SOCKS5: 176 alive / 160 gold

## Historical pool

- Discovered: 174836
- Ever alive: 33120
- Ever gold: 1226

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
