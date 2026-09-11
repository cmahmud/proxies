# SyndProxy validated proxy pool

## Current pool

- Alive now: 519
- Gold now: 445
- HTTP: 105 alive / 85 gold
- HTTPS: 52 alive / 28 gold
- SOCKS4: 177 alive / 161 gold
- SOCKS5: 185 alive / 171 gold

## Historical pool

- Discovered: 223440
- Ever alive: 49205
- Ever gold: 1575

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
