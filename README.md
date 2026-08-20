# SyndProxy private pool

## Current pool

- Alive now: 785
- Gold now: 384
- HTTP: 208 alive / 77 gold
- HTTPS: 171 alive / 21 gold
- SOCKS4: 209 alive / 142 gold
- SOCKS5: 197 alive / 144 gold

## Historical pool

- Discovered: 149514
- Ever alive: 26937
- Ever gold: 1089

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
