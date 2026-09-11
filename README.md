# SyndProxy validated proxy pool

## Current pool

- Alive now: 514
- Gold now: 429
- HTTP: 109 alive / 72 gold
- HTTPS: 39 alive / 20 gold
- SOCKS4: 178 alive / 164 gold
- SOCKS5: 188 alive / 173 gold

## Historical pool

- Discovered: 223440
- Ever alive: 48982
- Ever gold: 1570

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
