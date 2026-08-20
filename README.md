# SyndProxy private pool

## Current pool

- Alive now: 656
- Gold now: 392
- HTTP: 178 alive / 69 gold
- HTTPS: 80 alive / 16 gold
- SOCKS4: 196 alive / 151 gold
- SOCKS5: 202 alive / 156 gold

## Historical pool

- Discovered: 146662
- Ever alive: 25723
- Ever gold: 1073

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
