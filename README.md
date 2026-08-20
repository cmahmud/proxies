# SyndProxy private pool

## Current pool

- Alive now: 929
- Gold now: 393
- HTTP: 261 alive / 76 gold
- HTTPS: 202 alive / 24 gold
- SOCKS4: 232 alive / 142 gold
- SOCKS5: 234 alive / 151 gold

## Historical pool

- Discovered: 151072
- Ever alive: 27469
- Ever gold: 1097

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
