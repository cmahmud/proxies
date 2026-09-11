# SyndProxy validated proxy pool

## Current pool

- Alive now: 520
- Gold now: 443
- HTTP: 102 alive / 82 gold
- HTTPS: 53 alive / 31 gold
- SOCKS4: 175 alive / 160 gold
- SOCKS5: 190 alive / 170 gold

## Historical pool

- Discovered: 223440
- Ever alive: 49195
- Ever gold: 1575

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
