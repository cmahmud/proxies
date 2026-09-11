# SyndProxy validated proxy pool

## Current pool

- Alive now: 529
- Gold now: 450
- HTTP: 117 alive / 85 gold
- HTTPS: 51 alive / 28 gold
- SOCKS4: 173 alive / 161 gold
- SOCKS5: 188 alive / 176 gold

## Historical pool

- Discovered: 223440
- Ever alive: 49236
- Ever gold: 1575

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
