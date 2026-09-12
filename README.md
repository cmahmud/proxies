# SyndProxy validated proxy pool

## Current pool

- Alive now: 525
- Gold now: 444
- HTTP: 120 alive / 85 gold
- HTTPS: 44 alive / 28 gold
- SOCKS4: 180 alive / 162 gold
- SOCKS5: 181 alive / 169 gold

## Historical pool

- Discovered: 223440
- Ever alive: 49274
- Ever gold: 1575

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
