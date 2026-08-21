# SyndProxy private pool

## Current pool

- Alive now: 926
- Gold now: 402
- HTTP: 282 alive / 77 gold
- HTTPS: 169 alive / 22 gold
- SOCKS4: 242 alive / 161 gold
- SOCKS5: 233 alive / 142 gold

## Historical pool

- Discovered: 156828
- Ever alive: 29618
- Ever gold: 1133

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
