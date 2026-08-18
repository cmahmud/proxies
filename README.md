# SyndProxy private pool

## Current pool

- Alive now: 1099
- Gold now: 235
- HTTP: 429 alive / 24 gold
- HTTPS: 175 alive / 8 gold
- SOCKS4: 275 alive / 116 gold
- SOCKS5: 220 alive / 87 gold

## Historical pool

- Discovered: 86712
- Ever alive: 6879
- Ever gold: 320

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
