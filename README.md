# SyndProxy private pool

## Current pool

- Alive now: 1010
- Gold now: 386
- HTTP: 325 alive / 81 gold
- HTTPS: 221 alive / 25 gold
- SOCKS4: 213 alive / 144 gold
- SOCKS5: 251 alive / 136 gold

## Historical pool

- Discovered: 167112
- Ever alive: 32521
- Ever gold: 1185

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
