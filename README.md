# SyndProxy validated proxy pool

## Current pool

- Alive now: 664
- Gold now: 410
- HTTP: 152 alive / 75 gold
- HTTPS: 159 alive / 20 gold
- SOCKS4: 164 alive / 154 gold
- SOCKS5: 189 alive / 161 gold

## Historical pool

- Discovered: 190445
- Ever alive: 40262
- Ever gold: 1308

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
