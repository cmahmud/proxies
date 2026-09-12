# SyndProxy validated proxy pool

## Current pool

- Alive now: 529
- Gold now: 443
- HTTP: 122 alive / 85 gold
- HTTPS: 47 alive / 28 gold
- SOCKS4: 179 alive / 161 gold
- SOCKS5: 181 alive / 169 gold

## Historical pool

- Discovered: 223440
- Ever alive: 49273
- Ever gold: 1575

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
