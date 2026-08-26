# SyndProxy validated proxy pool

## Current pool

- Alive now: 543
- Gold now: 403
- HTTP: 103 alive / 65 gold
- HTTPS: 78 alive / 16 gold
- SOCKS4: 172 alive / 158 gold
- SOCKS5: 190 alive / 164 gold

## Historical pool

- Discovered: 185576
- Ever alive: 38703
- Ever gold: 1290

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
