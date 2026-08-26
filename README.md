# SyndProxy validated proxy pool

## Current pool

- Alive now: 662
- Gold now: 400
- HTTP: 138 alive / 76 gold
- HTTPS: 187 alive / 24 gold
- SOCKS4: 163 alive / 145 gold
- SOCKS5: 174 alive / 155 gold

## Historical pool

- Discovered: 190445
- Ever alive: 39989
- Ever gold: 1305

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
