# SyndProxy private pool

## Current pool

- Alive now: 698
- Gold now: 252
- HTTP: 202 alive / 32 gold
- HTTPS: 111 alive / 8 gold
- SOCKS4: 214 alive / 131 gold
- SOCKS5: 171 alive / 81 gold

## Historical pool

- Discovered: 94345
- Ever alive: 9682
- Ever gold: 373

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
