# SyndProxy validated proxy pool

## Current pool

- Alive now: 520
- Gold now: 451
- HTTP: 116 alive / 92 gold
- HTTPS: 49 alive / 31 gold
- SOCKS4: 173 alive / 161 gold
- SOCKS5: 182 alive / 167 gold

## Historical pool

- Discovered: 223440
- Ever alive: 49301
- Ever gold: 1576

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
