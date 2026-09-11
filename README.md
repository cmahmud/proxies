# SyndProxy validated proxy pool

## Current pool

- Alive now: 515
- Gold now: 425
- HTTP: 108 alive / 71 gold
- HTTPS: 38 alive / 19 gold
- SOCKS4: 181 alive / 163 gold
- SOCKS5: 188 alive / 172 gold

## Historical pool

- Discovered: 223440
- Ever alive: 48967
- Ever gold: 1569

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
