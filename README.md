# SyndProxy validated proxy pool

## Current pool

- Alive now: 521
- Gold now: 426
- HTTP: 111 alive / 71 gold
- HTTPS: 39 alive / 19 gold
- SOCKS4: 183 alive / 164 gold
- SOCKS5: 188 alive / 172 gold

## Historical pool

- Discovered: 223440
- Ever alive: 48968
- Ever gold: 1569

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
