# SyndProxy validated proxy pool

## Current pool

- Alive now: 523
- Gold now: 424
- HTTP: 91 alive / 71 gold
- HTTPS: 52 alive / 24 gold
- SOCKS4: 199 alive / 169 gold
- SOCKS5: 181 alive / 160 gold

## Historical pool

- Discovered: 223440
- Ever alive: 49085
- Ever gold: 1572

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
