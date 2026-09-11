# SyndProxy validated proxy pool

## Current pool

- Alive now: 510
- Gold now: 441
- HTTP: 110 alive / 80 gold
- HTTPS: 47 alive / 28 gold
- SOCKS4: 172 alive / 160 gold
- SOCKS5: 181 alive / 173 gold

## Historical pool

- Discovered: 223440
- Ever alive: 49213
- Ever gold: 1575

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
