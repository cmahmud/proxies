# SyndProxy private pool

## Current pool

- Alive now: 741
- Gold now: 328
- HTTP: 237 alive / 80 gold
- HTTPS: 132 alive / 20 gold
- SOCKS4: 173 alive / 105 gold
- SOCKS5: 199 alive / 123 gold

## Historical pool

- Discovered: 157573
- Ever alive: 29768
- Ever gold: 1137

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
