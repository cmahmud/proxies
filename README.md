# SyndProxy private pool

## Current pool

- Alive now: 890
- Gold now: 443
- HTTP: 268 alive / 99 gold
- HTTPS: 171 alive / 24 gold
- SOCKS4: 213 alive / 157 gold
- SOCKS5: 238 alive / 163 gold

## Historical pool

- Discovered: 167121
- Ever alive: 32537
- Ever gold: 1185

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
