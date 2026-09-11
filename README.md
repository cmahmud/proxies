# SyndProxy validated proxy pool

## Current pool

- Alive now: 529
- Gold now: 436
- HTTP: 105 alive / 74 gold
- HTTPS: 48 alive / 28 gold
- SOCKS4: 190 alive / 163 gold
- SOCKS5: 186 alive / 171 gold

## Historical pool

- Discovered: 223440
- Ever alive: 49149
- Ever gold: 1575

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
