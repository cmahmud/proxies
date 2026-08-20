# SyndProxy private pool

## Current pool

- Alive now: 978
- Gold now: 373
- HTTP: 325 alive / 72 gold
- HTTPS: 205 alive / 20 gold
- SOCKS4: 199 alive / 120 gold
- SOCKS5: 249 alive / 161 gold

## Historical pool

- Discovered: 148333
- Ever alive: 26104
- Ever gold: 1079

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
