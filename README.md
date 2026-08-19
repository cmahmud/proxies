# SyndProxy private pool

## Current pool

- Alive now: 1143
- Gold now: 594
- HTTP: 433 alive / 188 gold
- HTTPS: 298 alive / 129 gold
- SOCKS4: 203 alive / 133 gold
- SOCKS5: 209 alive / 144 gold

## Historical pool

- Discovered: 127345
- Ever alive: 19828
- Ever gold: 803

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
