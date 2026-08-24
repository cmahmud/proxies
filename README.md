# SyndProxy validated proxy pool

## Current pool

- Alive now: 551
- Gold now: 394
- HTTP: 122 alive / 58 gold
- HTTPS: 73 alive / 14 gold
- SOCKS4: 170 alive / 158 gold
- SOCKS5: 186 alive / 164 gold

## Historical pool

- Discovered: 179924
- Ever alive: 33522
- Ever gold: 1240

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
