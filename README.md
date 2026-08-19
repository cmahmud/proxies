# SyndProxy private pool

## Current pool

- Alive now: 1164
- Gold now: 590
- HTTP: 449 alive / 185 gold
- HTTPS: 300 alive / 129 gold
- SOCKS4: 205 alive / 133 gold
- SOCKS5: 210 alive / 143 gold

## Historical pool

- Discovered: 127345
- Ever alive: 19828
- Ever gold: 803

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
