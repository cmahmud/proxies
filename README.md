# SyndProxy validated proxy pool

## Current pool

- Alive now: 529
- Gold now: 449
- HTTP: 121 alive / 85 gold
- HTTPS: 53 alive / 31 gold
- SOCKS4: 173 alive / 162 gold
- SOCKS5: 182 alive / 171 gold

## Historical pool

- Discovered: 223440
- Ever alive: 49279
- Ever gold: 1575

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
