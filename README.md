# SyndProxy validated proxy pool

## Current pool

- Alive now: 538
- Gold now: 454
- HTTP: 115 alive / 83 gold
- HTTPS: 57 alive / 31 gold
- SOCKS4: 175 alive / 161 gold
- SOCKS5: 191 alive / 179 gold

## Historical pool

- Discovered: 223440
- Ever alive: 49221
- Ever gold: 1575

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
