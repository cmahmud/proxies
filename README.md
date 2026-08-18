# SyndProxy private pool

## Current pool

- Alive now: 1035
- Gold now: 368
- HTTP: 311 alive / 60 gold
- HTTPS: 241 alive / 14 gold
- SOCKS4: 249 alive / 151 gold
- SOCKS5: 234 alive / 143 gold

## Historical pool

- Discovered: 109322
- Ever alive: 15174
- Ever gold: 488

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
