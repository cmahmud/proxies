# SyndProxy validated proxy pool

## Current pool

- Alive now: 601
- Gold now: 343
- HTTP: 172 alive / 39 gold
- HTTPS: 63 alive / 9 gold
- SOCKS4: 173 alive / 151 gold
- SOCKS5: 193 alive / 144 gold

## Historical pool

- Discovered: 171044
- Ever alive: 32844
- Ever gold: 1212

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
