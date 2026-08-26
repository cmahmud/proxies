# SyndProxy validated proxy pool

## Current pool

- Alive now: 551
- Gold now: 412
- HTTP: 101 alive / 66 gold
- HTTPS: 82 alive / 17 gold
- SOCKS4: 177 alive / 161 gold
- SOCKS5: 191 alive / 168 gold

## Historical pool

- Discovered: 190445
- Ever alive: 39242
- Ever gold: 1297

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
