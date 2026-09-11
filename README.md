# SyndProxy validated proxy pool

## Current pool

- Alive now: 515
- Gold now: 446
- HTTP: 104 alive / 85 gold
- HTTPS: 51 alive / 28 gold
- SOCKS4: 176 alive / 161 gold
- SOCKS5: 184 alive / 172 gold

## Historical pool

- Discovered: 223440
- Ever alive: 49205
- Ever gold: 1575

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
