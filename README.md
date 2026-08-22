# SyndProxy private pool

## Current pool

- Alive now: 1005
- Gold now: 392
- HTTP: 332 alive / 83 gold
- HTTPS: 213 alive / 27 gold
- SOCKS4: 221 alive / 146 gold
- SOCKS5: 239 alive / 136 gold

## Historical pool

- Discovered: 167112
- Ever alive: 32526
- Ever gold: 1185

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
