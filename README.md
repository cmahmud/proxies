# SyndProxy private pool

## Current pool

- Alive now: 749
- Gold now: 370
- HTTP: 184 alive / 65 gold
- HTTPS: 165 alive / 18 gold
- SOCKS4: 208 alive / 151 gold
- SOCKS5: 192 alive / 136 gold

## Historical pool

- Discovered: 147686
- Ever alive: 25927
- Ever gold: 1076

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
