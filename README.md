# SyndProxy private pool

## Current pool

- Alive now: 959
- Gold now: 427
- HTTP: 298 alive / 105 gold
- HTTPS: 187 alive / 30 gold
- SOCKS4: 231 alive / 149 gold
- SOCKS5: 243 alive / 143 gold

## Historical pool

- Discovered: 160278
- Ever alive: 30761
- Ever gold: 1147

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
