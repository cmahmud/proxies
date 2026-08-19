# SyndProxy private pool

## Current pool

- Alive now: 946
- Gold now: 478
- HTTP: 304 alive / 123 gold
- HTTPS: 225 alive / 90 gold
- SOCKS4: 190 alive / 128 gold
- SOCKS5: 227 alive / 137 gold

## Historical pool

- Discovered: 117147
- Ever alive: 17556
- Ever gold: 671

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
