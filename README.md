# SyndProxy validated proxy pool

## Current pool

- Alive now: 621
- Gold now: 400
- HTTP: 118 alive / 73 gold
- HTTPS: 152 alive / 24 gold
- SOCKS4: 169 alive / 148 gold
- SOCKS5: 182 alive / 155 gold

## Historical pool

- Discovered: 190445
- Ever alive: 40148
- Ever gold: 1307

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
