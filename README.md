# SyndProxy validated proxy pool

## Current pool

- Alive now: 528
- Gold now: 403
- HTTP: 91 alive / 60 gold
- HTTPS: 80 alive / 20 gold
- SOCKS4: 171 alive / 159 gold
- SOCKS5: 186 alive / 164 gold

## Historical pool

- Discovered: 185576
- Ever alive: 38507
- Ever gold: 1290

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
