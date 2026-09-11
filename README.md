# SyndProxy validated proxy pool

## Current pool

- Alive now: 513
- Gold now: 435
- HTTP: 93 alive / 75 gold
- HTTPS: 51 alive / 26 gold
- SOCKS4: 184 alive / 163 gold
- SOCKS5: 185 alive / 171 gold

## Historical pool

- Discovered: 223440
- Ever alive: 49155
- Ever gold: 1575

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
