# SyndProxy private pool

## Current pool

- Alive now: 1060
- Gold now: 398
- HTTP: 359 alive / 84 gold
- HTTPS: 218 alive / 27 gold
- SOCKS4: 229 alive / 134 gold
- SOCKS5: 254 alive / 153 gold

## Historical pool

- Discovered: 166609
- Ever alive: 32419
- Ever gold: 1180

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
