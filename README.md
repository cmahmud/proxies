# SyndProxy validated proxy pool

## Current pool

- Alive now: 525
- Gold now: 435
- HTTP: 106 alive / 74 gold
- HTTPS: 45 alive / 27 gold
- SOCKS4: 189 alive / 163 gold
- SOCKS5: 185 alive / 171 gold

## Historical pool

- Discovered: 223440
- Ever alive: 49151
- Ever gold: 1575

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
