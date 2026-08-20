# SyndProxy private pool

## Current pool

- Alive now: 746
- Gold now: 386
- HTTP: 182 alive / 81 gold
- HTTPS: 152 alive / 20 gold
- SOCKS4: 219 alive / 144 gold
- SOCKS5: 193 alive / 141 gold

## Historical pool

- Discovered: 149512
- Ever alive: 26917
- Ever gold: 1089

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
