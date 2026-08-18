# SyndProxy private pool

## Current pool

- Alive now: 1002
- Gold now: 355
- HTTP: 322 alive / 57 gold
- HTTPS: 205 alive / 14 gold
- SOCKS4: 245 alive / 147 gold
- SOCKS5: 230 alive / 137 gold

## Historical pool

- Discovered: 107145
- Ever alive: 15126
- Ever gold: 483

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
