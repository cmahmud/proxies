# SyndProxy private pool

## Current pool

- Alive now: 1448
- Gold now: 590
- HTTP: 514 alive / 196 gold
- HTTPS: 445 alive / 91 gold
- SOCKS4: 242 alive / 145 gold
- SOCKS5: 247 alive / 158 gold

## Historical pool

- Discovered: 141229
- Ever alive: 24050
- Ever gold: 967

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
