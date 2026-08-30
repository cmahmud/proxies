# SyndProxy validated proxy pool

## Current pool

- Alive now: 530
- Gold now: 445
- HTTP: 116 alive / 82 gold
- HTTPS: 57 alive / 28 gold
- SOCKS4: 174 alive / 164 gold
- SOCKS5: 183 alive / 171 gold

## Historical pool

- Discovered: 199830
- Ever alive: 43691
- Ever gold: 1379

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
