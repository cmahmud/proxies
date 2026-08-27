# SyndProxy validated proxy pool

## Current pool

- Alive now: 633
- Gold now: 406
- HTTP: 103 alive / 62 gold
- HTTPS: 163 alive / 16 gold
- SOCKS4: 174 alive / 158 gold
- SOCKS5: 193 alive / 170 gold

## Historical pool

- Discovered: 190445
- Ever alive: 40741
- Ever gold: 1311

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
