# SyndProxy validated proxy pool

## Current pool

- Alive now: 524
- Gold now: 440
- HTTP: 115 alive / 84 gold
- HTTPS: 52 alive / 28 gold
- SOCKS4: 173 alive / 157 gold
- SOCKS5: 184 alive / 171 gold

## Historical pool

- Discovered: 223440
- Ever alive: 49273
- Ever gold: 1575

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
