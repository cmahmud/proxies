# SyndProxy private pool

## Current pool

- Alive now: 941
- Gold now: 403
- HTTP: 272 alive / 78 gold
- HTTPS: 185 alive / 22 gold
- SOCKS4: 250 alive / 161 gold
- SOCKS5: 234 alive / 142 gold

## Historical pool

- Discovered: 156828
- Ever alive: 29618
- Ever gold: 1133

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
